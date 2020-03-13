class Node:
    def __init__(self, val):
        self.val = val
        self.links = []
    def add_link(self, link):
        self.links.append(link)
    def __str__(self):
        node = "(%s):\n" % self.val
        for link in self.links:
            node += "\t" + link + "\n"
        return node
    def __add__(self, other):
        return str(self) + other
    def __radd__(self, other):
        return other + str(self)
    def equals(self, node):
        ok = (self.val == node.val)
        if len(self.links) == len(node.links):
            for i in range(len(self.links)):
                ok = ok and (self.links[i] == node.links[i])
            return ok
        else:
            return False

class Link:
    def __init__(self, from_node, etiquette, to_node):
        self.from_node = from_node
        self.etiquette = etiquette
        self.to_node = to_node
    def __str__(self):
        return "(%s --%s--> %s)" % (self.from_node.val, self.etiquette, self.to_node.val)
    def __add__(self, other):
        return str(self) + other
    def __radd__(self, other):
        return other + str(self)
    def equals(self, link):
        return (self.from_node == link.from_node) and (self.etiquette == link.etiquette) and (self.to_node == link.to_node)

class Automata:
    def __init__(self, initial_node, nodes, terminal_node, alphabet):
        self.initial_node = initial_node
        self.nodes = nodes
        self.terminal_node = terminal_node
        self.alphabet = alphabet
    def get_next_node(self, current_node, etiquette):
        for link in current_node.links:
            if link.etiquette == etiquette:
                return link.to_node
        return None
    def reconnaissance(self, string):
        node = self.initial_node
        for character in string:
            node = self.get_next_node(node, character)
        return self.terminal_node.equals(node)
        
    def reconnaissance_all_up_to_k(self, keme, k, string, node):
        #node = self.initial_node
        table = []
        if (self.terminal_node.equals(node)):
            table.append(string)
        if (keme == k):
            return table
        for character in self.alphabet:
            if self.get_next_node(node, character):
                new_node = self.get_next_node(node, character)
                string_out = string + character
                table += self.reconnaissance_all_up_to_k(keme + 1, k, string_out, new_node)
        return table

    def __str__(self):
        automata = "Initial node: %s\nTerminal node: %s\n" % (self.initial_node.val, self.terminal_node.val)
        for node in self.nodes:
            automata += node
        return automata
    def __add__(self, other):
        return str(self) + other
    def __radd__(self, other):
        return other + str(self)




if __name__ == '__main__':
    pass

    s0 = Node("s0")
    s1 = Node("s1")
    s2 = Node("s2")

    s0_a_s0 = Link(s0, 'a', s0)
    s0_b_s1 = Link(s0, 'b', s1)
    s1_a_s2 = Link(s1, 'a', s2)
    s1_b_s0 = Link(s1, 'b', s0)
    s2_a_s1 = Link(s2, 'a', s1)
    s2_b_s2 = Link(s2, 'b', s2)
    alphabet = ['a' , 'b']

    s0.add_link(s0_a_s0)
    s0.add_link(s0_b_s1)
    s1.add_link(s1_a_s2)
    s1.add_link(s1_b_s0)
    s2.add_link(s2_a_s1)
    s2.add_link(s2_b_s2)

    a = Automata(s0, [s0, s1, s2], s0, alphabet)

    print(a)
    print(a.reconnaissance('babbbabb')) #False
    table = []
    k = int(input("tapez k: "))
    table = a.reconnaissance_all_up_to_k(0, k, '', s0)
    print(table)

    ::change1