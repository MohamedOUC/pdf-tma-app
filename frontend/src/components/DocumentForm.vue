<template>
    <div class="form">
      <h2>Créer un document</h2>
      <form @submit.prevent="submitForm">
        <label>Titre :</label>
        <input v-model="title" type="text" required />

        <label>Contenu :</label>
        <textarea v-model="content" required></textarea>

        <label>Fichier :</label>
        <input type="file" @change="handleFileUpload"/>

        <button type="submit">Créer</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        title: '',
        content: '',
        file: null
      };
    },
    methods: {
      handleFileUpload(e) {
        this.file = e.target.files[0];
      },
      async submitForm() {
        const formData = new FormData();
        formData.append("title", this.title);
        formData.append("content", this.content);
        if(this.file) {
          formData.append("file", this.file);
        }
        
        const res = await fetch('http://localhost:8000/documents/uploads', {
          method: 'POST',
          body: formData
        });
        if (res.ok) {
          this.$emit('toast', {
            message: "Document créé avec succès ✅",
            type: "success"
          });
          this.title = '';
          this.content = '';
          this.file = null;
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