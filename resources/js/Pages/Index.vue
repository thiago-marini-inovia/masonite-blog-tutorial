<template>
  <div id="app">
    <h1>✨ Hot Reload is Working! Welcome {{ formatName(user) }}! ✨</h1>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      user: {
        firstName: 'Thi',
        lastName: 'Marini'
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