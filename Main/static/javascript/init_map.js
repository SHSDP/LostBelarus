ymaps.ready(init);
var myMap;
 function init(){
    // Создание карты.
    myMap = new ymaps.Map("map", {
        // Координаты центра карты.
        // Порядок по умолчанию: «широта, долгота».
        // Чтобы не определять координаты центра карты вручную,
        // воспользуйтесь инструментом Определение координат.
        center: [53.02712822957266, 27.551964649995742],
        // Уровень масштабирования. Допустимые значения:
        // от 0 (весь мир) до 19.
        zoom: 7
    });
    function add_marker(x, y, name){
      var placemark = new ymaps.Placemark(
          [x, y], // Координаты маркера
          { 
            hintContent: name, // Текст подсказки
          },
          {
            preset: 'islands#icon', // Предустановленный стиль маркера
            iconColor: '#0095b6' // Цвет маркера
          }
        );
      placemark.events.add('click',function(){
          window.location.href = 'arhetecture/1'
      })
      myMap.geoObjects.add(placemark);
  };
  window.add_marker = add_marker;
  
}   




    








