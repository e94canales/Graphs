def earliest_ancestor(ancestors, starting_node):
    # init children dictionary
    children = {}

    for ancestor in ancestors:
        if ancestor[1] not in children:
            # if child is not in d, add child as key and parent as value
            children[ancestor[1]] = [ancestor[0]]
        else:
            # else if it is in d, add parent to existing parents
            children[ancestor[1]].append(ancestor[0])

    # for e in children.items():
    #     print(f"**{e}")


    # if starting value doesnt have parents return -1
    if starting_node not in children:
        return -1

    # set current parents as starting childs parents - ie: 6 -> (3, 5)
    currentParents = children[starting_node]
    # print(currentParents)

    while True:
        # init new parents
        newParents = []

        # for each parent in current parents, if the parent has parents, set them as new parents
        for parent in currentParents:
            if parent in children:
                newParents += children[parent]
                print(newParents)

            # exit statement - return single value
            if len(newParents) < 1:
                return currentParents[0]

            # set new parents as current parents
            else:
                currentParents = newParents



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))