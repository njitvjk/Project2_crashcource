def loadmutant(filename):
    file = open('../calculator/test_results/' + filename + '.txt');
    lines = file.readlines();
    data = {};
    for line in lines:
        line = line.strip().split(",");
        test = line[0].strip();
        output = line[1].strip();
        data[test] = output;
    print(data)
    count = len(data);

    if count != 34:
        print(filename, count);
    return data;


def issame(res_a, res_b):
    print(res_a)

    print(res_b)
    # for t in res_a:
    if res_a == res_b:
        return True;
    return False;


base_results = loadmutant('Base');
# load the results of the base program

mutants = ['m' + str(i) for i in range(1, 21)];  # list of all mutants
results = {};
for m in mutants:
    results[m] = loadmutant(m);  # load the results of each mutant (test number: test outcome)
equivalent_mutants = {};
minimal_set = [];  # minimal set is initially empty
for m_a in mutants:  # for each mutant m_a
    to_add_m_a = True;
    for m_b in minimal_set:  # for each mutant in minimal set m_b
        if m_b == m_a:
            continue;
        if issame(results[m_a], results[m_b]):
            # if m_a and m_b are equivalent, don't add m_a to minimal set and add it to the equivalence class of m_b
            to_add_m_a = False;
            equivalent_mutants[m_b].append(m_a);
            break;
    if to_add_m_a:  # if m_a is not equivalent to any mutants in m_b, add it to the minimal set.
        minimal_set.append(m_a);
        equivalent_mutants[m_a] = [];

writer = open("analysis_equivalence.txt", "w");

writer.write("minimal set by equivalence:\n");
writer.write(", ".join(minimal_set) + "\n\n\n");

writer.write("Equivalent Classes:\n");
count = 1;
for m in equivalent_mutants:
    writer.write("Class " + str(count) + ": " + m + ", " + ", ".join(equivalent_mutants[m]) + "\n");
    count = count + 1;

writer.close();
