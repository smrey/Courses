# test dataset- load
dataset = "test.txt"


def simple():
    nodes_len_dict = {}
    with open(dataset, 'r') as d:
        for i, line in enumerate(d):
            if i == 0:
                num_leaves = line.rstrip()
            else:
                split_line = line.rstrip().split(":")
                nodes_len_dict[split_line[0]] = split_line[1]
    #print(num_leaves)  # matrix will be num_leaves x num_leaves
    #print(nodes_dict)

    # Find leaves (have only one connection)
    k_list = []
    for k in nodes_len_dict.keys():
        split_k = k.split("->")
        k_list.append(split_k)

    print(k_list)

        # Obtain list of all keys (once only)
        #nodes_dict =


def main():
    # Simplest solution first
    simple()


if __name__ == '__main__':
    main()

