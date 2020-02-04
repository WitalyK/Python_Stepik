with open('task2.html', 'w') as f:
    f.write('<html><body><table>\n')
    for i in range(1, 11):
        f.write('<tr>')
        for j in range(1, 11):
            f.write(f'<td>{i*j}</td>')
        f.write('</tr>\n')
    f.write('</table></body></html>')
