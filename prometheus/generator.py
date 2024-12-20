rule = """  - alert: HighRequestLatency_6h_#i#
    expr: avg_over_time(http_request_duration_seconds_sum{method="GET", endpoint="/api/v1/resource/#i#"}[6h]) > 50.00
    labels:
        severity: page
    annotations:
        summary: High request latency 2\n"""



# Open a file in write mode
with open('rules.yml', 'w') as file:
    # Write the group
    file.write('groups:\n')
    file.write('- name: team-A\n')
    file.write('  rules:\n')
    for i in range(1,5000):
        file.write(rule.replace("#i#", str(i)))

    

# The file is automatically closed when the block ends
