import os
from collections import defaultdict

from aste import common_path


def parse_metric(metric_name: str, perfromance_str: str):
    """

    :param metric_name:
    :param perfromance_str:
    :return:
    """
    start_index = perfromance_str.index(metric_name) + len(metric_name) + 1
    end_index = start_index + 5
    result = float(perfromance_str[start_index: end_index])
    return result


asote_test_result_filepath = os.path.join(common_path.project_dir, 'results/asote_results/results_test.csv')

results = defaultdict(dict)
with open(asote_test_result_filepath) as input_file:
    for line in input_file:
        if '"' not in line:
            continue
        parts = line.split(',')
        dataset_name = parts[2]
        performance = ','.join(parts[3:])
        precision = parse_metric('Precision', performance)
        recall = parse_metric('Recall', performance)
        f1 = parse_metric('FScore', performance)
        if 'p' not in results[dataset_name]:
            results[dataset_name]['p'] = []
        if 'r' not in results[dataset_name]:
            results[dataset_name]['r'] = []
        if 'f1' not in results[dataset_name]:
            results[dataset_name]['f1'] = []
        results[dataset_name]['p'].append(precision)
        results[dataset_name]['r'].append(recall)
        results[dataset_name]['f1'].append(f1)
for dataset_name, prf in results.items():
    for metric_name, metrics in prf.items():
        print('%s %s %s %s' % (dataset_name, metric_name, str(metrics), sum(metrics) / len(metrics)))
