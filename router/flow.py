import json

class FlowFlagStore:
    def __init__(self) -> None:
        self.flag_store = []
        self.flag_connection_sentences = []

    def flag_handler(self, original_predicted_sentence):
        with open('conversation.json', 'r', encoding='utf-8') as file:
            unfiltered_sentences = json.load(file)
        for unfiltered_index, unfiltered_val in enumerate(unfiltered_sentences):
            if original_predicted_sentence in unfiltered_val:
                flag = str(unfiltered_val).split(" | ")[2]
                result = self.flag_detecter(int(flag))
                result_sentence = self.A_modifier(result, original_predicted_sentence)
                print("\033[33m" + "LOG" + "\033[0m" + ":" + f"     Flag Store curret data: {str(self.flag_store)}")
                print("\033[33m" + "LOG" + "\033[0m" + ":" + f"     Flag Connection Sentences curret data: {str(self.flag_connection_sentences)}")
                return result_sentence

    def flag_detecter(self, flag):
        if flag == 6:
            try:
                self.flag_store.index(flag - 1)
                self.flag_store.append(flag)
                return 1
            except ValueError:
                return -1
        else:
            try:
                self.flag_store.index(flag - 1)
                self.flag_store.append(flag)
                return 0
            except ValueError:
                if flag in (0, 1, 2, 3):
                    self.flag_store.append(flag)
                    return 0
                else:
                    return -1
                
    def A_modifier(self, result, original_predicted_sentence):
        if result == -1:
            return -1
        elif result == 1:
            return_sentence = self.extract_beverage_kind()
            self.flag_store = []
            self.flag_connection_sentences = []
            return return_sentence
        else:
            self.flag_connection_sentences.append(original_predicted_sentence)
            return 0
        
    def extract_beverage_kind(self):
        return_sentence = ""
        for flag_store_index, flag_store_val in enumerate(self.flag_store):
            if flag_store_val == 3:
                beverage = str(self.flag_connection_sentences[flag_store_index]).split(" 줄래?")[0] 
            elif flag_store_val == 4:
                amount = str(self.flag_connection_sentences[flag_store_index]).split(' 줘')[0]
                total = " " + beverage +  " " + amount
                return_sentence += total
        return "카드를 삽입해주십시오." + return_sentence + " 결제가 완료되었습니다. 방문해주셔서 감사합니다."
