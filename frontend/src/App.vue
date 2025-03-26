<template>
  <div id="app">
    <header>
      <h1>📄 App </h1>
    </header>

    <main>
      <DocumentForm @toast="handleToast" />
      <hr />
      <DocumentSearch @toast="handleToast" />
    </main>
    <Toast v-if="toast.message" :message="toast.message" :type="toast.type" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import DocumentForm from './components/DocumentForm.vue'
import DocumentSearch from './components/DocumentSearch.vue'
import Toast from './components/Toast.vue'

const toast = ref({ message: '', type: 'success' })

function handleToast({ message, type }) {
  toast.value = { message, type }
  setTimeout(() => (toast.value.message = ''), 3000)
}
</script>

<style scoped>
body {
  background: #f5f6fa;
  color: #333;
}

input, textarea, button {
  font-size: 1rem;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

button {
  cursor: pointer;
  background-color: #007bff;
  color: white;
  border: none;
  transition: background-color 0.2s ease;
}

button:hover {
  background-color: #0056b3;
}

h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #007bff;
}
</style>
