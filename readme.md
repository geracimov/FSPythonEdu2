# linguisticCodeReport


### Инфо
Получение отчета об использовании частей речи в названиях указанных структур языка
  
на текущий момент функциональность реализована для :
* систем управления версиями: git
* части речи: глагол и существительное
* поиск проходит в названиях переменных и функций
* вывод осуществляется в: json,csv,console
* пасинг для языка программирования: python

### Запуск 
```
usage: reports.py [-h] --repotype {git,svn} --repourl REPOURL --speechparts
                  {verb,noun} [{verb,noun} ...]
                  [--scope {vars,funcs} [{vars,funcs} ...]] --output
                  {json,csv,console} --lang {python,java}
```

