
(function() {
    'use strict';
    
    angular
        .module('app')
        .controller('SpeakersController', SpeakersController);
        
    SpeakersController.$inject = ['$location', 'common', 'config', 'datacontext'];
    function SpeakersController($location, common, config, datacontext) {
        //jshint valid this: true
        var vm = this;
        var keyCodes = config.keyCodes;
        
        vm.filteredSpeakers = [];
        vm.gotoSpeaker =gotoSpeaker;
        vm.refresh = refresh;
        vm.search = search;
        vm.speakerSearch = '';
        vm.speakers = [];
        vm.title = 'Speakers';
    }
    
    function gotoSpeaker() {
        //code
    }
    function refresh() {
        //code
    }
    function search() {
        //code
    }
    
    activate();
    function activate() {
        //code
        getSpeakers();
    }
    function applyFilter(){
        //code
        vm.filteredSpeaakers = vm.speakers.filter(speakerFilter);
    }
    
    function AvengersController(avengersService, logger) {
        //code
        var vm = this;
        vm.avengers = [];
        vm.getAvengers = getAvengers;
        vm.title = 'Avengers';
        
        activate();
        
        function activate() {
            //code
            return getAvengers().then(function(){
                logger.info('Activated Avengers View');
            });
        }
        
        function getAvengers() {
            //code
            return avengersService.getAvengers().then(function(data){
                vm.avengers = data;
                return vm.avengers;
            });
        }
    }
    
    function OrderController(creditService) {
        //code
        var vm =this;
        vm.checkCredit = checkCredit;
        vm.isCreditOk;
        vm.total = 0;
        
        function checkCredit() {
            //code
            return creditService.isOrderTotalOk(vm.total)
                    .then(function(isOk) { vm.isCreditOk = isOk; })
                    .catch(showError);
        };
    }
    
})();