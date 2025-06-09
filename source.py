import csv
from statistics import mean
from collections import OrderedDict


def calculate_averages(input_file_name, output_file_name):
    name_gpa = OrderedDict()
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 1:
                name = row[0]
                grades = [int(grade) for grade in row[1:]]
                gpa = mean(grades)
                name_gpa[name] = gpa

    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for name, gpa in name_gpa.items():
            writer.writerow([name, f"{gpa:.1f}" if gpa % 1 == 0 else gpa])


def calculate_sorted_averages(input_file_name, output_file_name):
    name_gpa = {}
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 1:  # بررسی خطوط دارای حداقل یک نام و یک نمره
                name = row[0]
                grades = [int(grade) for grade in row[1:]]
                gpa = mean(grades)
                name_gpa[name] = gpa

    sorted_names_gpa = sorted(name_gpa.items(), key=lambda item: (item[1], item[0]))

    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for name, gpa in sorted_names_gpa:
            writer.writerow([name, f"{gpa:.1f}" if gpa % 1 == 0 else gpa])



def calculate_three_best(input_file_name, output_file_name):
    name_gpa = {}
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 1:
                name = row[0]
                grades = [int(grade) for grade in row[1:]]
                gpa = mean(grades)
                name_gpa[name] = gpa

    sorted_names_gpa = sorted(name_gpa.items(), key=lambda item: (-item[1], item[0]))
    top_3 = sorted_names_gpa[:3]

    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for name, gpa in top_3:
            writer.writerow([name, f"{gpa:.1f}" if gpa % 1 == 0 else gpa])



def calculate_three_worst(input_file_name, output_file_name):
    name_gpa = {}
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 1:
                name = row[0]
                grades = [int(grade) for grade in row[1:]]
                gpa = mean(grades)
                name_gpa[name] = gpa

    sorted_names_gpa = sorted(name_gpa.items(), key=lambda item: (item[1], item[0]))
    bottom_3 = sorted_names_gpa[:3]

    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for _, gpa in bottom_3:
            writer.writerow([f"{gpa:.1f}" if gpa % 1 == 0 else gpa])



def calculate_average_of_averages(input_file_name, output_file_name):
    gpa_list = []
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 1:
                grades = [int(grade) for grade in row[1:]]
                gpa = mean(grades)
                gpa_list.append(gpa)

    average_of_averages = mean(gpa_list)

    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f"{average_of_averages:.1f}" if average_of_averages % 1 == 0 else average_of_averages])

