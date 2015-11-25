app.controller('PostController', ['$scope', 'directory', '$routeParams', function($scope, directory, $routeParams) {
  directory.success(function(data) {
    $scope.post = data[$routeParams.id];
  });
}]);
