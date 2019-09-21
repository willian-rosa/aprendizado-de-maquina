from ann import Ann
import numpy as np

class BackPropagation(Ann):
    @staticmethod
    def _sigmoid(x):
        return 1.0/(1.0+np.exp(-x))

    def run(self, inputs, output_training, nn, seasons, alfa):

        stopping = False

        layer_size = len(nn)

        for season in range(seasons):

            z_input = [[0 for z_i in range(len(nn[z_i][0]))] for z_i in range(layer_size)]
            z = [[0 for z_i in range(len(nn[z_i][0]))] for z_i in range(layer_size)]

            for i_input, input_val in enumerate(inputs):  # para cada par de treinamento

                # ativando os neuronios

                for layer in range(layer_size):

                    if layer == 0:
                        input_layer = input_val
                    else:
                        input_layer = z[layer-1]

                    for z_j in range(len(nn[layer][0])):
                        for i, x in enumerate(input_layer):  # cada caracter da letra
                            z_input[layer][z_j] = z_input[layer][z_j] + x * nn[layer][i][z_j]

                        z[layer][z_j] = self._sigmoid(z_input[layer][z_j])

                # calculando erro
                exit_layer = layer_size-1

                # passo 6

                delta_w = []
                delta_ks = [0 for z_i in range(len(z[exit_layer]))]

                for i, y in enumerate(z[exit_layer]):

                    sigmoid_t = self._sigmoid(z_input[exit_layer][i])
                    delta_ks[i] = (output_training[i_input][i] - y) * sigmoid_t * (1-sigmoid_t)

                for j, z_j in enumerate(z[exit_layer-1]):  # TODO ficou estranho
                    delta_w.append([])
                    for delta_k in delta_ks:
                        delta_w[j].append(alfa * delta_k * z_j)

                delta_input_js = [0, 0, 0]

                # passo 7

                for j, z_j in enumerate(delta_w):
                    for k, delta_k in enumerate(delta_ks):
                        delta_input_js[j] = delta_input_js[j] +  delta_k * delta_w[j][k]

                delta_v = []

                for i, x_i in enumerate(input_val):  # TODO ficou estranho
                    delta_v.append([])
                    for delta_j in delta_input_js:
                        delta_v[i].append(alfa * delta_j * x_i)


                # passo 8
                # TODO código duplicado os 2 seguintes for
                for j, w in enumerate(nn[1]):
                    for k, w_k in enumerate(w):
                        nn[1][j][k] = nn[1][j][k] + delta_w[j][k]

                for i, v in enumerate(nn[0]):
                    for j, v_j in enumerate(v):
                        nn[0][i][j]  = nn[0][i][j] + delta_v[i][j]

    def run2(self):
        pass
