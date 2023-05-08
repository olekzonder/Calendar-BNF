import re
import sys
import graphviz

class CalendarParser:
    def __init__(self, text):
        self.text = text
        self.events = []
    def parse(self):
        self.name = 'событие'
        self.k = 1
        self.events = {}
        self.events['календарь'] = []
        lines = self.text.split(';')
        for line in lines:
            event = self.parse_event(line.strip())
            if event:
                self.events['календарь'].append(event)
        return self.events

    def parse_event(self, line):
        match = re.match(r'(\d{2} \w+ \d{4}):\s*(\d{2}):(\d{2})(.*)', line)
        if not match:
            return None
        date_str, hour_str, minute_str, description = match.groups()
        try:
            day, month, year = self.parse_date(date_str)
            hour, minute = int(hour_str), int(minute_str)
        except ValueError:
            return None
        return {'событие':{'дата':{'день':day, 'месяц':month, 'год':year}, 'время':{'час':hour, 'минуты':minute}, 'описание':{'текст':description.strip()}}}

    def parse_date(self, date_str):
        parts = date_str.split()
        day = int(parts[0])
        month_name = parts[1]
        month = self.parse_month(month_name)
        year = int(parts[2])
        return day, month, year

    def parse_month(self, month_name):
        months = {
            'января': 1,
            'февраля': 2,
            'марта': 3,
            'апреля': 4,
            'мая': 5,
            'июня': 6,
            'июля': 7,
            'августа': 8,
            'сентября': 9,
            'октября': 10,
            'ноября': 11,
            'декабря': 12,
        }
        return months.get(month_name.lower(), -1)
# Example usage
with open(sys.argv[1]) as data:
    text = data.read()
parser = CalendarParser(text)
events = parser.parse()

def print_tree(data, indent=0):
    if isinstance(data, dict):
        for key, value in data.items():
            print("{}{}:".format("\t" * indent, key))
            print_tree(value, indent + 1)
    elif isinstance(data, list):
        for item in data:
            print_tree(item, indent + 1)
    else:
        print("{}{}".format("\t" * indent, data))

from graphviz import Digraph

def draw_tree(tree, graph=None, parent=None, counter=None):
    if graph is None:
        graph = Digraph()
    for key, value in tree.items():
        node_name = str(key)
        if counter is not None and node_name in counter:
            counter[node_name] += 1
            node_name += '_' + str(counter[node_name])
        elif counter is not None:
            counter[node_name] = 1
        if parent is not None:
            graph.edge(str(parent), node_name)
        if isinstance(value, dict):
            draw_tree(value, graph, node_name, counter)
        elif isinstance(value, list):
            for item in value:
                draw_tree(item, graph, node_name, counter)
        else:
            graph.node(node_name, label=str(value))
    return graph


print_tree(events)
dot = draw_tree(events,counter={})
dot.format = "png"
dot.render(sys.argv[1].split('.')[0])

print("Файл сохранён как ",sys.argv[1].split('.')[0],".png",sep='')
