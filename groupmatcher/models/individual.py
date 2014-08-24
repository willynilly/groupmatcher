class Individual:
    def __init__(self, id, group_pref_values=None):
        self.id = str(id)
        self.group_pref_values = group_pref_values
        if not self.group_pref_values:
            self.group_pref_values = {}
    
    def set_group_pref_value(self, group_id, value):
        self.group_pref_values[str(group_id)] = float(value)
        
    def get_group_pref_value(self, group_id):
        return float(self.group_pref_values[str(group_id)])