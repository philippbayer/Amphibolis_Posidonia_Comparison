ara_genes = {}
for line in open('NC_000932.1.gff3'):
    ll = line.split()
    if len(ll) < 3: continue
    thistype = ll[2]
    if thistype != 'gene':
        continue
    # ['NC_000932.1', 'Chloe', 'gene', '14024', '14770', '.', '-', '.', 'ID=atpI;Name=atpI']
    start = ll[3]
    end = ll[4]
    length = abs(int(end) - int(start))
    name = ll[-1].split(';')[0].replace('ID=','')
    ara_genes[name] = length


from glob import glob
from collections import defaultdict
for l in glob('*gff3'):
    if 'NC' in l: continue
    thisgenes = defaultdict(int)
    print('----')
    print(l)
    for line in open(l):
        ll = line.split()
        if len(ll) < 3: continue
        thistype = ll[2]
        if thistype != 'gene':
            continue
        # ['NC_000932.1', 'Chloe', 'gene', '14024', '14770', '.', '-', '.', 'ID=atpI;Name=atpI']
        start = ll[3]
        end = ll[4]
        length = abs(int(end) - int(start))
        name = ll[-1].split(';')[1].replace('Name=','')
        thisgenes[name] = length

    for ara_gene in sorted(ara_genes.keys()):
        perc_diff = abs(ara_genes[ara_gene] - thisgenes[ara_gene]) / ara_genes[ara_gene] * 100
        print(ara_gene, ara_genes[ara_gene], thisgenes[ara_gene], '%.1f'%perc_diff)
