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

2.1.1. API для списка заказов возвращает элементы со след. атрибутами: дата заказа, цвет, марка авто, модель авто, количество
<p align="center">
<img src="https://github.com/zorokonStepan/CarDealer_DjangoDRFOpenApiSwagger/raw/main/img_git/api/api_get.png" width="450"
title="api_get">
</p>

2.1.2. В случае не передачи даты заказа в запросе заказ создается с текущей датой.
<p align="center">
<img src="https://github.com/zorokonStepan/CarDealer_DjangoDRFOpenApiSwagger/raw/main/img_git/api/api_post.png" width="450"
title="api_post">
</p>

2.1.3. Пример обновления заказа.
<p align="center">
<img src="https://github.com/zorokonStepan/CarDealer_DjangoDRFOpenApiSwagger/raw/main/img_git/api/api_patch.png" width="450"
title="api_patch">
</p>

2.1.4. Пример удаления заказа.
<p align="center">
<img src="https://github.com/zorokonStepan/CarDealer_DjangoDRFOpenApiSwagger/raw/main/img_git/api/api_delete.png" width="450"
title="api_delete">
</p>

С остальными моделями аналогично.

2.2. Реализовать API для получения след. информации:

2.2.1. Список цветов с указанием количества заказанных авто каждого цвета (атрибуты элементов: цвет, количество)
<p align="center">
<img src="https://github.com/zorokonStepan/CarDealer_DjangoDRFOpenApiSwagger/raw/main/img_git/api/api_color_count.png" width="450"
title="api_color_count">
</p>

2.2.2. Список марок с указанием количества заказанных авто каждой марки (атрибуты элементов: марка, количество)
<p align="center">
<img src="https://github.com/zorokonStepan/CarDealer_DjangoDRFOpenApiSwagger/raw/main/img_git/api/api_brand_count.png" width="450"
title="api_brand_count">
</p>

2.3. Обеспечить пользовательское представление API в формате OpenApi (Swagger).
<p align="center">
<img src="https://github.com/zorokonStepan/CarDealer_DjangoDRFOpenApiSwagger/raw/main/img_git/swagger_open_api/swagger1.png" width="450"
title="swagger open api">
</p>

<p align="center">
<img src="https://github.com/zorokonStepan/CarDealer_DjangoDRFOpenApiSwagger/raw/main/img_git/swagger_open_api/swagger2.png" width="450"
title="swagger open api">
</p>