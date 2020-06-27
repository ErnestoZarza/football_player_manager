from pulp import *

from data_manager import DataManager


class TeamBuilder:
    def __init__(self):
        self.data_manager = DataManager()

    # Solution as a knapsack problem with restrictions using LP.
    def team_builder(self, budget):
        defender_pos = ['RCB', 'CB', 'LB', 'RB', 'RWB', 'LWB']
        middle_pos = ['RCM', 'LCM', 'LDM', 'CDM', 'LCB', 'RM', 'LM', 'RDM', 'CM']
        forward_pos = ['RF', 'ST', 'LW', 'LF', 'RS', 'CAM', 'LS', 'LAM', 'RW', 'RAM', 'CF']

        data = self.data_manager.get_data_frame_from_db()

        player = [str(i) for i in range(data.shape[0])]
        point = {str(i): data['Overall'][i] for i in range(data.shape[0])}
        value = {str(i): data['Value'][i] for i in range(data.shape[0])}
        gk = {str(i): 1 if data['Position'][i] == 'GK' else 0 for i in range(data.shape[0])}
        fullback = {str(i): 1 if data['Position'][i] in defender_pos else 0 for i in range(data.shape[0])}
        halfback = {str(i): 1 if data['Position'][i] in middle_pos else 0 for i in range(data.shape[0])}
        forward = {str(i): 1 if data['Position'][i] in forward_pos else 0 for i in range(data.shape[0])}
        xi = {str(i): 1 for i in range(data.shape[0])}

        prob = LpProblem("Knapsack_Football", LpMaximize)
        player_vars = LpVariable.dicts("Players", player, 0, 1, LpBinary)

        # objective function
        prob += lpSum([point[i] * player_vars[i] for i in player]), "Total_Cost"

        # constraint
        prob += lpSum([player_vars[i] for i in player]) == 11, "Total_11_Players"
        prob += lpSum([value[i] * player_vars[i] for i in player]) <= budget, "Total_Cost"
        prob += lpSum([gk[i] * player_vars[i] for i in player]) == 1, "1_GK"
        prob += lpSum([fullback[i] * player_vars[i] for i in player]) == 2, "2_DEF"
        prob += lpSum([halfback[i] * player_vars[i] for i in player]) == 3, "3_MID"
        prob += lpSum([forward[i] * player_vars[i] for i in player]) == 5, "5_STR"

        # solve
        status = prob.solve()
        player_index_list = []
        for v in prob.variables():
            if v.varValue > 0:
                index = str(v.name).replace("Players_", '')
                player_index_list.append(int(index))

        result = data.iloc[player_index_list]
        return result


if __name__ == "__main__":
    builder = TeamBuilder()
    players = builder.team_builder(200000000)
    print(players)
    # print(players.describe())
