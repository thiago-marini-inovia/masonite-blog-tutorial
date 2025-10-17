<template>
    
    <div>
      <h1> Hellow, {{ formatName(user) }}! </h1>
    </div>
  </template>
  
  <script>
  export default {
    name: 'app',
    data() {
      return {
        user: {
          firstName: 'Harry',
          lastName: 'Manchanda'
        }
      };
    },
    methods: {
      formatName(user) {
        return `${user.firstName} ${user.lastName}`;
      }
    }
  }
  </script>
  
  <style lang="scss">
  </style>