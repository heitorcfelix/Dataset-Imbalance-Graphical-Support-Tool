# Dataset-Imbalance-Graphical-Suport-Tool
Projeto desenvolvido para a disciplina de Visualização de dados do CIn-UFPE, semestre 2020.1.

## TODO list
### class imbalance
- [ ] agrupar classes pequenas no piechart
- [ ] ativar detalhamento das classes pequenas mostrando nova piechart
- [x] implementar gráfico de numero de objetos por imagem
- [ ] implementar gráfico de quantas imagens do total contém ao menos 1 exemplo da classe (por classe)
### scale imbalance
- [x] colocar texto sobre small e big bboxes
- [x] ordenar classes: small-medium-big
- [x] tratar dados para o gráfico de coordenadas paralelas
- [x] implementar gráfico de coordenadas paralelas
- [x] corrigir seleção da coordenada de classes
- [x] implementar interação com seleção das classes (do primeiro gráfico)
### object location imbalance
- [x] tratar dados para formação dos heatmaps
- [x] implementar heatmaps
- [ ] exibir eixos junto do heatmap (incluindo o de escala)
- [ ] adicionar título com a classe representada em cada heatmap
- [ ] colocar interação com a seleção do primeiro gráfico do dashboard
### general
- [x] esconder inputs do scale imbalance quando inicia a página
- [ ] organizar layout da página como um todo