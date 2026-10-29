from django.shortcuts import get_object_or_404, render
from .forms import ApplicationForm
from .models import JobListing


def job_list(request):
    jobs = JobListing.objects.filter(is_active=True).order_by('-created_at')
    context = {
        'jobs': jobs
    }
    return render(request, 'jobs/job_list.html', context)

def job_detail(request, pk):
    # Mengambil lowongan berdasarkan ID (primary key), jika tidak ada muncul error 404
    job = get_object_or_404(JobListing, pk=pk, is_active=True)
    context = {
        'job': job
    }
    return render(request, 'jobs/job_detail.html', context)
# ... (biarkan fungsi job_list dan job_detail yang sudah ada tetap di sini) ...

def apply_job(request, pk):
    job = get_object_or_404(JobListing, pk=pk, is_active=True)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return render(request, 'jobs/apply_success.html', {'job': job})
    else:
        form = ApplicationForm()

    context = {
        'job': job,
        'form': form
    }
    return render(request, 'jobs/apply_form.html', context)