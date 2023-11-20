all_types=set()
# all types are

# {'clade', 'subphylum', 'genus', 'tribe', 'order', 'superkingdom', 'species', 'suborder', 'class', 'subclass', 'subfamily', 'family', 'phylum', 'varietas', 'kingdom'}
TOKEEP = set(['superkingdom', 'class', 'order', 'family', 'genus', 'species'])

with open('all_cat.summary.tsv') as fh:
    header = fh.readline().rstrip().split('\t')
    print('\t'.join(header[:-1]) + '\tSuperkingdom\tClass\tOrder\tFamily\tGenus\tSpecies')
    for line in fh:
        ll = line.rstrip().split('\t')
        lineages = ll[6:]
        this_types = {}
        for l in lineages:
            thistype = l.split(':')[0].split('(')[-1].replace(')', '')
            l = l.replace(f' ({thistype})', '')

            if thistype == 'no rank': continue
            if thistype in TOKEEP:
                if thistype in this_types:
                    this_types[thistype] = this_types[thistype] + ', ' + l
                else:
                    this_types[thistype] = l

        for a in TOKEEP:
            if a not in this_types:
                this_types[a] = 'NA'
        newll = [this_types[i] for i in ['superkingdom', 'class', 'order', 'family', 'genus', 'species']]
        print('\t'.join(ll[:6]) +'\t'+ '\t'.join(newll))
