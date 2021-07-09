<script>
/*eslint no-console: ["error", { allow: ["warn", "error"] }] */

export default {
  name: "app",
  data() {
    return {
      appTitle: 'Take Home _ vuejs-src-App.vue',
    };
  },
};
</script>

<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title>{{appTitle}}</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-content>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-content>

    <v-footer app></v-footer>
  </v-app>
</template>
