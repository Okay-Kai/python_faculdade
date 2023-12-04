from collections import namedtuple

Estoque = namedtuple('Estoque', ['Higiene', 'Limpeza', 'Alimentício'])
compras_hig = ['pasta de dente', 'papel higiênico', 'fio dental', 'sabonete']
compras_lim = ['agua sanitaria', 'desinfetante', 'sabao em pó']
compras_ali = ['arroz', 'feijao', 'ovo', 'batata', 'macarrao']
Est = Estoque(compras_hig, compras_lim, compras_ali)