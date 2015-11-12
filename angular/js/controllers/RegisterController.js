app.controller('RegisterController', ['$scope', 'username', function($scope, username) {
  emails.success(function(data) {
    $scope.username = data;
  });
}]);
