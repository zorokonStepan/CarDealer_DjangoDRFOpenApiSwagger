ТЗ в ReadmeTasks.md<br>
Инструкция по запуску в ReadmeStart.md<br>

<h1>Реализовано</h1>
<br>
Окружение.<br>
1. Python == 3.9.7<br>
2. Postgres == 14.5<br>
3. Django == 4.1.2<br>
4. djangorestframework==3.14.0<br>
5. drf-yasg==1.21.4 - Swagger
<br><br>
1. Созданы модели согласно ТЗ.<br>

1.1. Реализована пагинация списка заказов (объем страницы 10 элементов)
<p align="center">
<img src="https://github.com/zorokonStepan/CarDealer_DjangoDRFOpenApiSwagger/raw/main/img_git/pag1.png" width="450"
title="pagination">
</p>

1.2. Реализована сортировка списка заказов по количеству.
<p align="center">
<img src="https://github.com/zorokonStepan/CarDealer_DjangoDRFOpenApiSwagger/raw/main/img_git/sort_cnt.png" width="450"
title="count sorted">
</p>

1.3. Реализована фильтрация списка заказов по марке авто.
<p align="center">
<img src="https://github.com/zorokonStepan/CarDealer_DjangoDRFOpenApiSwagger/raw/main/img_git/sort_brand1.png" width="450"
title="brand sorted">
</p>

<p align="center">
<img src="https://github.com/zorokonStepan/CarDealer_DjangoDRFOpenApiSwagger/raw/main/img_git/sort_brand2.png" width="450"
title="brand sorted">
</p>

2. С использованием библиотеки Django Rest Framework создано RestAPI для управления справочниками и заказами согласно ТЗ.<br>

2.1. API для списка заказов возвращает элементы со след. атрибутами: дата заказа, цвет, марка авто, модель авто, количество
<p align="center">
<img src="https://github.com/zorokonStepan/CarDealer_DjangoDRFOpenApiSwagger/raw/main/img_git/api/api_get.png" width="450"
title="api_get">
</p>

2.2. В случае не передачи даты заказа в запросе заказ создается с текущей датой.
<p align="center">
<img src="https://github.com/zorokonStepan/CarDealer_DjangoDRFOpenApiSwagger/raw/main/img_git/api/api_post.png" width="450"
title="api_post">
</p>


