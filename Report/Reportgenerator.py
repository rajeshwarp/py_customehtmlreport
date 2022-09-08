import pandas as pd
import jinja2
from jinja2 import FileSystemLoader

tests = []
suiteName = ''
suiteDescription = ''

df = pd.read_json('TestCase.json')

# Retrieve Tests in a List
for row in df.iterrows():
    tests.append(row[1].testCases)

suiteDescription = df['suiteDescription'][0]
suiteName = df['suiteName'][0]
testCount = len(tests)

# Template handling
loader = FileSystemLoader('Report')
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=''))
template = env.get_template('template.html')
html = template.render(
    tests=tests,
    suiteName=suiteName,
    testCount=testCount,
    suiteDescription=suiteDescription,

)

# print(html)
with open('results.html', 'w') as f:
    f.write(html)
