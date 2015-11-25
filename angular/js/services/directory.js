app.factory('directory', ['$http', function($http) {
  return $http.get('js/services/topics.html')
            .success(function(data) {
              return data;
            })
            .error(function(err) {
              return err;
            });
}]);
