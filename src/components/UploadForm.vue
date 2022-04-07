<template>
  <div class="row">
    <div class="col-sm-12 col-md-6">
      <div class="container">
        <h1 class="mb-5">Upload Photo</h1>
        <form
          enctype="multipart/form-data"
          id="uploadForm"
          @submit.prevent="uploadPhoto"
        >
          <div class="form-group my-5">
            <div class="form-label">Upload Photo</div>
            <input name="photo" type="file" class="form-control" />
          </div>

          <div class="form-group my-5">
            <div class="form-label text-bold">Description</div>
            <textarea name="description" type="text" class="form-control" />
          </div>

          <div class="d-block w-100">
            <button type="submit" class="btn btn-dark float-right">
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>



<script>
export default {
  data() {
    return {
      csrf_token: "",
    };
  },

  methods: {
    uploadPhoto() {
      const uploadForm = document.getElementById("uploadForm");
      let form_data = new FormData(uploadForm);

      console.log(form_data.get('photo'))

      fetch("/api/upload", {
        method: "POST",
        body: form_data,
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
        })
        .catch((error) => console.log(error));
    },

    getCsrfToken() {
      fetch("/api/csrf-token")
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          this.csrf_token = data.csrf_token;
        })
        .catch((error) => console.log(error));
    },
  },

  created() {
    this.getCsrfToken();
  },
};
</script>