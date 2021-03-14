from Classes.DecisionsData import DecisionsData

inputs_data, actions_data = DecisionsData()

class DecisionMachine:
    
    def search_action(self, text):
        for inp in inputs_data:
            if inp in text:
                return inputs_data[inp]

        return 'nothing'

    def answer(self, text):
        inp = self.search_action(text)
        if inp == 'nothing':
            return None
        action = actions_data[inp]
        if not action['parameters']:
            return action['function']()
        else:
            return action['function'](text)
    


    
