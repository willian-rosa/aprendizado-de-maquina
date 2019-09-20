import numpy as np

class Ann:

    """
    O mapeamento de deve seguir a quantidade de itens de cada camada
    Ex:
    3 para entrada, 3 para camada intermediaria 1, 3 para camada intermediaria 2, 2 saidas
    [3, 3, 3, 2]

    Ex:
    3 para entrada, 3 para camada intermediaria, 2 saidas
    [3, 3, 2]
    """
    @staticmethod
    def create_ann(config: list):

        network = []

        for index_config, value_config in enumerate(config):

            if len(config)-1 > index_config:

                network.append(
                    # gerando matriz
                    np.random.uniform(-1, 1, [value_config, config[index_config+1]])
                )

        return network
