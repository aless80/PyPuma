from pypuma.puma import Puma
puma_obj = Puma('ToyData/ToyExpressionData.txt', 'ToyData/ToyMotifData.txt', 'ToyData/ToyPPIData.txt','ToyData/ToyMiRList.txt')
puma_obj.save_puma_results('Toy_Puma.pairs.txt')
puma_obj.top_network_plot(top=70, file='top_genes.png')
indegree = puma_obj.return_puma_indegree()
outdegree = puma_obj.return_puma_outdegree()
