<template>
  <div class="search">
    <h2>🔍 Rechercher un document</h2>
    <form @submit.prevent="search">
      <input v-model="searchTitle" type="text" placeholder="Mot-clé du titre" />
      <button type="submit">Rechercher</button>
    </form>

    <div v-if="results && results.length">
      <h3>📄 Résultats :</h3>
      <ul>
        <li v-for="doc in results" :key="doc.id">
          <div v-if="editingId !== doc.id">
            <strong>{{ doc.title }}</strong><br />
            {{ doc.content }}<br />
            <button @click="startEdit(doc)">✏️ Modifier</button>
            <button @click="deleteDocument(doc.id)">🗑️ Supprimer</button>
          </div>
  
          <div v-else>
            <input v-model="editTitle" placeholder="Titre" />
            <textarea v-model="editContent" placeholder="Contenu"></textarea><br />
            <button @click="saveEdit(doc.id)">💾 Enregistrer</button>
            <button @click="cancelEdit()">❌ Annuler</button>
          </div>
        </li>
      </ul>
    </div>

    <p v-else-if="searched">Aucun résultat trouvé.</p>

    <!-- ✅ Modale personnalisée -->
    <div v-if="showModal" class="modal-overlay">
      <div class="modal-content">
        <p>Confirmer la suppression du document ?</p>
        <button @click="confirmDelete">Oui</button>
        <button @click="cancelDelete">Non</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchTitle: '',
      results: [],
      searched: false,
      editingId: null,
      editTitle: '',
      editContent: '',
      showModal: false,
      docToDelete: null
    };
  },
  methods: {
    async search() {
      this.searched = true;
      const res = await fetch(`http://localhost:8000/documents/search?title=${encodeURIComponent(this.searchTitle)}`);
      if (res.ok) {
        this.results = await res.json();
        console.log("Résultats : ", this.results);
      }
    },
    startEdit(doc) {
      this.editingId = doc.id;
      this.editTitle = doc.title;
      this.editContent = doc.content;
    },
    cancelEdit() {
      this.editingId = null;
      this.editTitle = '';
      this.editContent = '';
    },
    async saveEdit(id) {
      const res = await fetch(`http://localhost:8000/documents/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          title: this.editTitle,
          content: this.editContent
        })
      });
      if (res.ok) {
        const updated = await res.json();
        const index = this.results.findIndex(doc => doc.id === id);
        this.results[index] = updated;
        this.cancelEdit();
      }
    },
    deleteDocument(id) {
      this.docToDelete = id;
      this.showModal = true;
    },
    async confirmDelete() {
      const res = await fetch(`http://localhost:8000/documents/${this.docToDelete}`, { method: 'DELETE' });
      if (res.ok) {
        this.results = this.results.filter(doc => doc.id !== this.docToDelete);
        this.$emit('toast', { message: 'Document supprimé', type: 'success' });
      } else {
        this.$emit('toast', { message: 'Erreur lors de la suppression', type: 'error' });
      }
      this.showModal = false;
      this.docToDelete = null;
    },
    cancelDelete() {
      this.showModal = false;
      this.docToDelete = null;
    }
  }
};
</script>

<style scoped>
li {
  color: white !important;
  opacity: 1 !important;
  display: block;
  font-size: 16px;
  background-color: #2b2b2b;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
}
li div strong, li div span, li div {
  color: white !important;
  opacity: 1!important;
  background: #444;
  padding: 8px;
  border-radius: 4px;
}
.search {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
}
input {
  width: 70%;
  padding: 6px;
  margin-right: 10px;
}
button {
  padding: 6px 10px;
}
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(9, 9, 9, 0.899);
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal-content {
  background: rgb(14, 14, 14);
  padding: 20px;
  border-radius: 8px;
}
</style>
