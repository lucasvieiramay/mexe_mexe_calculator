from dataclasses import dataclass
from typing import Dict, ClassVar


@dataclass
class Player:
    name: str
    points: int
    eliminated: bool = False

    def __repr__(self):
        return player.name

    def add_point(self, points: int):
        self.points += points
        if self.points > 199:
            print('Jogador está eliminado')
            self.eliminated = True


if __name__ == '__main__':
    players = input('Digite o nome dos jogadores separados por ,')
    players = players.split(',')
    players_obj = []
    for i, player in enumerate(players):
        point = int(input(f'Digite a pontuação do jogador {player}'))
        players_obj.append(Player(name=player, points=point))

    round = 1
    while True:
        round += 1
        print(f'Rodada {round}')
        print('-------------')
        for player in players_obj:
            if player.eliminated:
                continue
            point = input(f'Digite a pontuação do jogador {player}')
            player.add_point(points=int(point))

        print('Pontuação da rodada:')
        for player in players_obj:
            if player.eliminated:
                continue
            print(f'{player}: {player.points}')
        print('---------------------')
