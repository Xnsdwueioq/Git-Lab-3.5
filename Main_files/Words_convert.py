import json
from random import randint

data = {
  "абстракция": "отделение существенного от несущественного, обобщение.",
  "баланс": "состояние равновесия между различными элементами.",
  "вектор": "направление и величина в пространстве.",
    "гипотеза": "предположение, требующее проверки.",
  "дилемма": "ситуация, в которой необходимо выбрать одно из двух трудных решений.",
  "инновация": "введение нового, улучшение существующего.",
  "критерий": "основание для оценки или суждения.",
  "метафора": "переносное значение слова или выражения.",
  "норматив": "правило или стандарт, определяющий нормы поведения.",
  "оптимизация": "процесс улучшения чего-либо для достижения наилучшего результата.",
  "парадигма": "модель, образец, система взглядов.",
  "космос": "вселенная, пространство вне Земли.",
  "синергия": "взаимодействие, при котором сумма эффектов больше, чем сумма отдельных эффектов.",
  "потенциал": "возможность, способность к развитию.",
  "интерпретация": "толкование, объяснение чего-либо.",
  "реакция": "ответ на какое-либо воздействие.",
  "трансформация": "преобразование, изменение формы или состояния.",
  "концепция": "основная идея, замысел.",
  "феномен": "явление, которое требует объяснения.",
  "дискуссия": "обсуждение различных точек зрения.",
  "эксперимент": "практическое исследование для проверки гипотезы.",
  "анализ": "разделение целого на части для изучения.",
  "система": "совокупность взаимосвязанных элементов.",
  "моделирование": "создание модели для изучения процессов.",
  "интеграция": "объединение частей в единое целое.",
  "категория": "группа объектов с общими признаками.",
  "структура": "организация элементов в целое.",
  "параметр": "переменная, определяющая характеристики системы.",
  "функция": "назначение, роль элемента в системе.",
  "доктрина": "система взглядов и убеждений.",
  "комплексность": "сложность системы или явления.",
  "интервал": "промежуток времени или пространства.",
  "механизм": "система взаимодействующих частей для выполнения задачи.",
  "катализатор": "вещества, ускоряющие химическую реакцию без изменения себя.",
  "прогноз": "предсказание о будущем на основе анализа данных.",
  "индикатор": "показатель состояния или уровня чего-либо.",
  "стратегия": "план действий для достижения цели.",
  "долговечность": "способность сохранять свои свойства в течение времени.",
  "конкуренция": "соперничество между участниками рынка.",
  "параллель": "сходство, аналогия между явлениями.",
  "классика": "произведения искусства или литературы, признанные образцовыми.",
  "глобализация": "процесс интеграции стран и народов в мировую экономику и культуру.",
  "квалификация": "уровень подготовки и знаний специалиста.",
  "эволюция": "процесс постепенных изменений и развития.",
  "технология": "методы и средства производства или обработки информации.",
  "поток": "непрерывное движение чего-либо в одном направлении.",
  "тренд": "направление изменений в определенной области.",
  "результат": "итог какого-либо действия или процесса.",
  "коммуникация": "обмен информацией между людьми или системами.",
  "аналогия": "сходство между различными предметами или явлениями.",
  "принцип": "основное правило или закон, на котором основано действие.",
  "определение": "точное указание значения слова или термина.",
  "экспертиза": "оценка профессионалов в определенной области.",
  "аргументация": "представление доводов в поддержку своей позиции.",
    "консенсус": "общее согласие группы людей по какому-либо вопросу.",
  "симптом": "признак, указывающий на наличие болезни или проблемы.",
  "факт": "доказанное событие или состояние дел.",
  "достоверность": "надежность и правдивость информации.",
  "коллаборация": "совместная работа над проектом или задачей.",
  "доступность": "легкость доступа к ресурсам или услугам.",
  "декларация": "официальное заявление о намерениях или позициях.",
  "инфраструктура": "совокупность объектов и систем, обеспечивающих функционирование общества.",
  "мультидисциплинарный": "объединяющий несколько дисциплин или областей знаний.",
  "технологичность": "степень применения современных технологий.",
  "экспертность": "уровень знаний и навыков в определенной области.",
  "юридическая": "относящийся к праву или правовым нормам.",
  "блокчейн": "распределенная база данных для хранения информации о транзакциях.",
  "влияние": "способность оказывать воздействие на что-либо или кого-либо.",
  "гипотетический": "основанный на предположениях, а не на фактах.",
  "критичность": "способность оценивать ситуации с разных точек зрения.",
  "недостаток": "отсутствие необходимых качеств или ресурсов.",
  "объективность": "независимость от личных мнений и предвзятостей.",
  "параметризация": "определение параметров для анализа системы.",
  "тенденция": "направление изменений в определенной области.",
  "феноменология": "научное изучение явлений как они воспринимаются человеком.",
  "юриспруденция": "наука о праве и правовых системах.",
  "аргумент": "довод, служащий основанием для утверждения или мнения.",
  "базовый": "основной, фундаментальный для понимания темы.",
  "алгоритм": "Последовательность шагов для решения задачи.",
  "библиотека": "Собрание функций и методов, которые можно использовать в программе.",
  "веб-разработка": "Создание и поддержка веб-сайтов.",
  "декомпозиция": "Разделение задачи на более мелкие подзадачи.",
  "документация": "Описание функциональности программы и её компонентов.",
  "зависимость": "Связь между модулями или библиотеками.",
  "изменяемый": "Объект, который можно изменять после его создания.",
  "интерфейс": "Определение методов, которые должен реализовать класс.",
  "класс": "Шаблон для создания объектов с общими свойствами и методами.",
  "компиляция": "Процесс преобразования исходного кода в исполняемый файл.",
  "конструктор": "Метод, который вызывается при создании объекта.",
  "логика": "Правила и условия, определяющие поведение программы.",
  "массив": "Структура данных, хранящая элементы одного типа.",
  "метод": "Функция, связанная с объектом или классом.",
  "модуль": "Файл с кодом, который можно импортировать в другие файлы.",
  "наследование": "Механизм, позволяющий создавать новый класс на основе существующего.",
  "объект": "Экземпляр класса с состоянием и поведением.",
  "прием": "Метод или техника, используемая для решения задачи.",
  "прототип": "Предварительная версия программы или компонента.",
  "проектирование": "Создание структуры и архитектуры программы.",
  "проверка": "Процесс тестирования и оценки функциональности программы.",
  "разработка": "Процесс создания программного обеспечения.",
  "синтаксис": "Правила написания кода на языке программирования.",
  "тестирование": "Процесс проверки программы на наличие ошибок.",
  "экспорт": "Процесс вывода данных из программы или модуля.",
  "инкапсуляция": "Сокрытие внутреннего состояния объекта от внешнего мира.",
  "асинхронность": "Возможность выполнения задач независимо друг от друга.",
  "параллелизм": "Одновременное выполнение нескольких задач или процессов.",
  "событие": "Действие, которое программа может обрабатывать (например, нажатие клавиши)."
}
with open('Words.json', 'w') as fp:
    json.dump(data, fp)
with open('Words.json', 'r') as fp:
    words_json = json.load(fp)
    keys_list = [key for key in words_json.keys()]
    value_list = [words_json[key] for key in keys_list]


for _ in range(250):
  randint(250, 2457)
