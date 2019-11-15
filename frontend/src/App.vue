<template>
  <div id="app">
    <form>
      <label for="title">Title</label>
      <input type="text" v-model="formData.title" name="title" />
      <label for="content">Content</label>
      <textarea v-model="formData.content" name="content"></textarea>

      <br />

      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      formData: {
        title: '',
        content: ''
      }
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  max-width: 500px;
  margin: 0 auto;
  text-align: left;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
  input, textarea {
    width: 100%;
    display: block;
    padding: 6px 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  label {
    margin-top: 15px;
    display: block;
  }
  button {
    background: #000;
    color: #fff;
    border-radius: 3px;
    padding: 6px 10px;
  }
</style>
