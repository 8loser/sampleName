# SampleName
產生隨機英文名稱或英文名稱的中文翻譯

[![PyPI](https://img.shields.io/pypi/v/SampleName.svg)](https://pypi.org/project/SampleName/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/SampleName.svg)


# Install
```
pip install SampleName
```

# Using

```
from sampleName import SampleName

smapleName = SampleName()
nameList = smapleName.listNameEng()
print(nameList)
# ['Kate', 'Cedric', 'Adrian', 'Yuri', 'Lara', 'Mildred', 'Craig', 'Oswald']

nameList = smapleName.listNameCht()
print(nameList)
# ['海頓', '藍道夫', '吉羅德', '妮可拉', '阿爾瓦', '比尤萊', '伊蒂絲', '珀莉']
```

# Development

 - VSCode
 - 開發環境佈置 [Remote-Containers](https://8loser.github.io/2022/05/13/Remote-Containers/)
   - 執行 remote container 會自動安裝 flake8, yapf 套件, 以及 pytest
 - 單元測試, 執行 `pytest`
   - [test_sampleName.py](/tests/test_sampleName.py)
 - release 後會自動上傳到 PyPI, 版本號會用 tag
   - [release_action.yml](/.github/workflows/release_action.yml)
   - [setup.py](/setup.py)
