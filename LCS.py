import sys
script_name = sys.argv
arg1 = sys.argv[1]
arg2 = sys.argv[2]
def find_lcs(dna1, dna2):
    m = len(dna1)
    n = len(dna2)
    lcs = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dna1[i - 1] == dna2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    result = ""
    i, j = m, n
    while i > 0 and j > 0:
        if dna1[i - 1] == dna2[j - 1]:
            result = dna1[i - 1] + result
            i -= 1
            j -= 1
        elif lcs[i - 1][j] > lcs[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
    return lcs[m][n], result

def print_lcs(dna1, dna2):
    m = len(dna1)
    n = len(dna2)
    lcs = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dna1[i - 1] == dna2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    result = ""
    i, j = m, n
    while i > 0 and j > 0:
        if dna1[i - 1] == dna2[j - 1]:
            result = dna1[i - 1] + result
            i -= 1
            j -= 1
        elif lcs[i - 1][j] > lcs[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return result

def compare_dna(body_dna_file, parent_dna_file, output_file):
    with open(body_dna_file, 'r') as body_file, open(parent_dna_file, 'r') as parent_file, open(output_file, 'w') as output:
        body_dna = body_file.readline().strip()
        parent_dna = parent_file.readline().strip()
        output.write("body_dna \t parent_dna \t lcs_length \t lcs_string \n")
        output.write("-"*60 + "\n")
        while parent_dna:
            lcs_length, lcs_string = find_lcs(body_dna, parent_dna)
            
            output.write(f"{body_dna} \t {parent_dna} \t {lcs_length} \t {lcs_string}\n")
            parent_dna = parent_file.readline().strip()


def main():
    body_dna = 'uploads/' + arg1
    parent_dna = 'uploads/' + arg2
    output_file = 'public/result.txt'
    compare_dna(body_dna, parent_dna, output_file)
    f = open('public/result.txt', 'r')
    print(f.read())
if __name__ == '__main__':
    main()