angular.module('spicyApp1', [])
.controller('SpicyController', ['$scope', function($scope){
    $scope.spice = "very";
    $scope.chiliSpicy = function() {
        $scope.spice = "Chili";
    };
    $scope.jalapenoSpicy = function() {
        $scope.spice = "Jalapeno";
    };
}]);