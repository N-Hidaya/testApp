var myApp = angular.module('scopeInheritance', []);
myApp.controller('MainController', ['$scope', function($scope){
    $scope.timeOfDay = "morning";
    $scope.name = "Melissa";
}]);

myApp.controller('ChildController', ['$scope', function($scope){
    //time of day follows MainController: morning
    $scope.name = "Roberts";
}]);

myApp.controller('GrandchildController', ['$scope', function($scope){
    $scope.timeOfDay = "evening";
    $scope.name = "Amy";
}]);
