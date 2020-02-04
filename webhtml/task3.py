with open('task3.html', 'w') as f:
    f.write('<html><body><table>\n')
    for i in range(1, 11):
        f.write('<tr>')
        for j in range(1, 11):
            f.write(f'<td><a href=http://{i*j}.ru>{i*j}</a></td>')
        f.write('</tr>\n')
    f.write('</table></body></html>')
s = 'Python'
ans = 0
for c in s:
    ans = ans * 123417 + ord(c)
print(ans)

'2290710658703611189398393962'