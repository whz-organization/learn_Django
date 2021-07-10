<script>
/*eslint no-console: ["error", { allow: ["warn", "error"] }] */

import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      courses: [],
      headers: [
        {
          text: 'ID',
          align: 'start',
          sortable: true,
          value: 'id',
        },
        {
          text: 'Name',
          sortable: true,
          value: 'name',
        },
        { text: 'Actions', value: 'actions', sortable: false },
      ],
    };
  },
  mounted() {
    axios
      .get('http://127.0.0.1:8000/api/courses/')
      .then(response => this.courses = response.data)
  },
};
</script>

<template>
  <div class="container">
    <h2>Course Listings</h2>
    
    <v-card
      v-if="!courses || courses.length === 0"
      key="notPresent"
      class="p-10"
      >You have no courses yet! _ axios -> 405 error</v-card
    >

    <v-data-table
      v-if="courses && courses.length"
      :headers="headers"
      :items="courses"
      class="elevation-1"
    >
      <template v-slot:item.actions="{ item }">
        <v-icon
          small
          class="mr-2"
        >
          mdi-pencil
        </v-icon>
        <v-icon
          small
        >
          mdi-delete
        </v-icon>
      </template>
    </v-data-table>
  </div>
</template>

<style scoped>
.p-10 {
  padding: 10px;
}
</style>