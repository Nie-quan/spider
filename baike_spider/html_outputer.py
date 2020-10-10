from urllib.parse import unquote


class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def output_html(self):

        with open('output.html', 'w', encoding='utf-8') as fout:
            fout.write('<html>')
            fout.write('<body>')
            fout.write('<table border="1" cellspacing="0" cellpadding="0">')

            for data in self.datas:
                fout.write('<tr>')
                fout.write(f'<td>{unquote(data["url"], encoding="utf-8")}</td>')
                fout.write(f'<td>{data["title"]}</td>')
                fout.write(f'<td>{data["summary"]}</td>')
                fout.write('</tr>')

            fout.write('</table>')
            fout.write('</body>')
            fout.write('</html>')

    def collect_data(self, data):
        if data is None:
            return

        self.datas.append(data)
        # print('self.datas: ', self.datas)
