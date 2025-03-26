<template>
    <div class="form">
      <h2>Créer un document</h2>
      <form @submit.prevent="submitForm">
        <label>Titre :</label>
        <input v-model="title" type="text" required />
        <label>Contenu :</label>
        <textarea v-model="content" required></textarea>
        <button type="submit">Créer</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        title: '',
        content: ''
      };
    },
    methods: {
      async submitForm() {
        const res = await fetch('http://localhost:8000/documents/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ title: this.title, content: this.content })
        });
        if (res.ok) {
          this.$emit('toast', {
            message: "Document créé avec succès ✅",
            type: "success"
          });
          this.title = '';
          this.content = '';
        } else {
          this.$emit('toast', {
            message: "Erreur lors de la création ❌",
            type: "error"
          });
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .form {
    max-width: 500px;
    margin: auto;
    padding: 20px;
  }
  input, textarea {
    width: 100%;
    margin-bottom: 10px;
  }
  </style>  