app.controller('TopicController', ['$scope', 'directory', function($scope, directory) {
  directory.success(function(data) {
    $scope.directory = data.results;
  });
}]);
