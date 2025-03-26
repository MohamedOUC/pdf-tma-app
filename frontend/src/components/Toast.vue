<template>
    <div v-if="visible" class="toast" :class="type">
      {{ message }}
    </div>
  </template>
  
  <script>
  export default {
    props: {
      message: String,
      type: {
        type: String,
        default: 'success' // success, error...
      }
    },
    data() {
      return {
        visible: true
      };
    },
    mounted() {
      setTimeout(() => {
        this.visible = false;
      }, 3000);
    }
  }
  </script>
  
  <style scoped>
  .toast {
    position: fixed;
    bottom: 30px;
    right: 30px;
    padding: 12px 20px;
    border-radius: 8px;
    color: white;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    animation: fadeIn 0.3s ease;
    z-index: 1000;
  }
  .success {
    background-color: #28a745;
  }
  .error {
    background-color: #dc3545;
  }
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  </style>  