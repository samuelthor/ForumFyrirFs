app.controller('LoginController', ['$scope', 'username', function($scope, username) {
  emails.success(function(data) {
    $scope.username = data;
  });
}]);
