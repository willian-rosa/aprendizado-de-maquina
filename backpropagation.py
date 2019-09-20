from ann import Ann
import numpy as np

class BackPropagation(Ann):
    @staticmethod
    def _sigmoid(x):
        return 1.0/(1.0+np.exp(-x))

    def run(self, inputs, output_training, nn):

        stopping = False

        layer_size = len(nn)
        alfa = 1

        while not stopping:

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

                for j, z_j in enumerate(delta_w):
                    for k, delta_k in enumerate(delta_ks):
                        delta_input_js[j] = delta_input_js[j] +  delta_k * delta_w[j][k]
                        # print(delta_input_js[j], delta_w[j][k])
                    print(delta_input_js[j])

                    # error[layer][]
            exit(2)




    def run2(self):
        pass
